'use client'

import { Input } from '@/components/ui/input'
import { api } from '@/lib/axios'
import { getErrorMessage } from '@/lib/utils'
import { useMutation } from '@tanstack/react-query'
import { AxiosError } from 'axios'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { useState } from 'react'
import { useForm } from 'react-hook-form'

interface RegisterForm {
  email: string
  password: string
  confirm_password: string
  first_name: string
  last_name: string
  shop_name: string
}

export default function RegisterPage() {
  const router = useRouter()
  const [error, setError] = useState('')
  const { register, handleSubmit, formState: { isSubmitting } } = useForm<RegisterForm>()

  const registerMutation = useMutation({
    mutationFn: async (data: RegisterForm) => {
      const response = await api.post('/auth/register/', {
        ...data,
        confirm_password: data.confirm_password
      })
      return response.data
    },
    onSuccess: () => {
      router.push('/login')
    },
    onError: (error: AxiosError) => {
      setError(getErrorMessage(error))
    },
  })

  const onSubmit = (data: RegisterForm) => {
    if (data.password !== data.confirm_password) {
      setError('Passwords do not match')
      return
    }
    setError('')
    registerMutation.mutate(data)
  }

  return (
    <div className="flex min-h-screen flex-col justify-center bg-gradient-to-br from-blue-50 to-indigo-50 px-6 py-12 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="animate-fade-in space-y-6 rounded-xl bg-white/80 px-8 py-10 shadow-2xl backdrop-blur-lg">
          <div className="space-y-2 text-center">
            <h1 className="text-3xl font-bold tracking-tight text-gray-900">
              Create Account
            </h1>
            <p className="text-sm text-gray-600">
              Join ShopKeeper Pro to manage your business better
            </p>
          </div>

          <form className="space-y-6" onSubmit={handleSubmit(onSubmit)}>
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label
                    htmlFor="first_name"
                    className="block text-sm font-medium text-gray-700"
                  >
                    First Name
                  </label>
                  <div className="mt-1">
                    <Input
                      id="first_name"
                      type="text"
                      required
                      className="form-input"
                      placeholder="John"
                      {...register('first_name')}
                    />
                  </div>
                </div>
                <div>
                  <label
                    htmlFor="last_name"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Last Name
                  </label>
                  <div className="mt-1">
                    <Input
                      id="last_name"
                      type="text"
                      required
                      className="form-input"
                      placeholder="Doe"
                      {...register('last_name')}
                    />
                  </div>
                </div>
              </div>

              <div>
                <label
                  htmlFor="shop_name"
                  className="block text-sm font-medium text-gray-700"
                >
                  Shop Name
                </label>
                <div className="mt-1">
                  <Input
                    id="shop_name"
                    type="text"
                    required
                    className="form-input"
                    placeholder="My Shop"
                    {...register('shop_name')}
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Email
                </label>
                <div className="mt-1">
                  <Input
                    id="email"
                    type="email"
                    required
                    className="form-input"
                    placeholder="john@example.com"
                    {...register('email')}
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="password"
                  className="block text-sm font-medium text-gray-700"
                >
                  Password
                </label>
                <div className="mt-1">
                  <Input
                    id="password"
                    type="password"
                    required
                    className="form-input"
                    {...register('password')}
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="confirm_password"
                  className="block text-sm font-medium text-gray-700"
                >
                  Confirm Password
                </label>
                <div className="mt-1">
                  <Input
                    id="confirm_password"
                    type="password"
                    required
                    className="form-input"
                    {...register('confirm_password')}
                  />
                </div>
              </div>
            </div>

            {error && (
              <div className="rounded-md bg-red-50 p-4">
                <div className="flex">
                  <div className="flex-shrink-0">
                    <svg
                      className="h-5 w-5 text-red-400"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                  <div className="ml-3">
                    <p className="text-sm text-red-700">{error}</p>
                  </div>
                </div>
              </div>
            )}

            <div>
              <button
                type="submit"
                disabled={isSubmitting}
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50"
              >
                {isSubmitting ? 'Creating Account...' : 'Create Account'}
              </button>
            </div>
          </form>

          <p className="text-center text-sm text-gray-600">
            Already have an account?{' '}
            <Link
              href="/login"
              className="font-semibold text-indigo-600 hover:text-indigo-500"
            >
              Login here
            </Link>
          </p>
        </div>
      </div>
    </div>
  )
}
